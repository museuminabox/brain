"""Detects current RaspberryPi version from `/proc/cpuinfo`"""
import re


__version__ = '0.1.1'


REVISION_INFO = {
    # Revision:Release Date/Model/PCB Revision/Memory/Notes
    'Beta':   ['Q1 2012', 'B (Beta)',   '?',   '256 MB', 'Beta Board'],
    '0002':   ['Q1 2012', 'B',          '1.0', '256 MB', None],
    '0003':   ['Q3 2012', 'B (ECN0001)' '1.0', '256 MB', 'Fuses mod and D14 removed'],
    '0004':   ['Q3 2012', 'B',          '2.0', '256 MB', 'Mfg by Sony'],
    '0005':   ['Q4 2012', 'B',          '2.0', '256 MB', 'Mfg by Qisda'],
    '0006':   ['Q4 2012', 'B',          '2.0', '256 MB', 'Mfg by Egoman'],
    '0007':   ['Q1 2013', 'A',          '2.0', '256 MB', 'Mfg by Egoman'],
    '0008':   ['Q1 2013', 'A',          '2.0', '256 MB', 'Mfg by Sony'],
    '0009':   ['Q1 2013', 'A',          '2.0', '256 MB', 'Mfg by Qisda'],
    '000d':   ['Q4 2012', 'B',          '2.0', '512 MB', 'Mfg by Egoman'],
    '000e':   ['Q4 2012', 'B',          '2.0', '512 MB', 'Mfg by Sony'],
    '000f':   ['Q4 2012', 'B',          '2.0', '512 MB', 'Mfg by Qisda'],
    '0010':   ['Q3 2014', 'B+',         '1.0', '512 MB', 'Mfg by Sony'],
    '0011':   ['Q2 2014', 'Compute Module', '1.0', '512 MB',  'Mfg by Sony'],
    '0012':   ['Q4 2014', 'A+',         '1.0', '256 MB', 'Mfg by Sony'],
    '0013':   ['Q1 2015', 'B+',         '1.2', '512 MB', ''],
    'a01041': ['Q1 2015', '2 Model B',  '1.1', '1 GB',   'Mfg by Sony'],
    'a21041': ['Q1 2015', '2 Model B',  '1.1', '1 GB',   'Mfg by Embest, China'],
    '900092': ['Q4 2015', 'Zero',       '1.2', '512 MB', 'Mfg by Sony'],
    '900093': ['Q2 2016', 'Zero',       '1.3', '512 MB', 'Mfg by Sony'],
    'a02082': ['Q1 2016', '3 Model B',  '1.2', '1024 MB','Mfg by Sony'],
    'a22082': ['Q1 2016', '3 Model B',  '1.2', '1024 MB','Mfg by ?'],
}


def get_rpi_revision():
    """Returns the version number from the revision line."""
    for line in open("/proc/cpuinfo"):
        if "Revision" in line:
            return re.sub('Revision\t: ([a-z0-9]+)\n', r'\1', line)


if __name__ == '__main__':
    try:
        revision = get_rpi_revision()
        rpi_info = REVISION_INFO[revision]
    except KeyError:
        print("Not on a Raspberry Pi")
    else:
        print("""Revision:     {}
Release date: {}
Model:        {}
PCB Revision: {}
Memory:       {}
Notes:        {}""".format(revision, *rpi_info))
