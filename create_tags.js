// Script to generate NDEF records for Museum in a Box
// 
// Takes a CSV as input
// Generates files which can be used by libfreefare's
// example/mifare-classic-write-ndef utility to write to
// Mifare classic tags

//var csv_file = "women.csv"
//var csv_file = "animals.csv"
var csv_file = "gypsum.csv"
var output_directory = "tags"

var csv = require("csv");
var fs = require('fs');
var ndef = require('ndef');

var parser = csv.parse({delimiter: ','}, function(err, data) {
    //console.log(data);
    for (record in data) {
        //console.log("Record:");
        //console.log("=> "+data[record][0]);
        var message = [ndef.uriRecord(data[record][1]),
            ndef.textRecord("{\"id\":"+data[record][2]+",\"audio\":\""+data[record][3]+"\",\"video\":\""+data[record][4]+"\"}") ];
        var byteArray = ndef.encodeMessage(message);
        var buf = new Buffer(byteArray);
        var tag_filename = output_directory+"/"+data[record][2]+".ndef";
        fs.writeFileSync(tag_filename, buf);
        //console.log("Ready to write "+data[record][0]);
        //console.log("Place a tag onto the reader and hit ENTER to continue...");
        //execSync("sudo ../libfreefare/examples/mifare-classic-write-ndef -i "+tag_filename);
        console.log("echo About to write "+data[record][0]);
        console.log("read");
        console.log("sudo ../libfreefare/examples/mifare-classic-write-ndef -i "+tag_filename);
    }
});

fs.createReadStream(csv_file).pipe(parser);


