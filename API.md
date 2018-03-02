# Cloud API

These are the calls the box expects to be able to call in the cloud service, in order to administer the box.

## Record Boop

POST https://museuminabox.herokuapp.com/boops

### Submits

Example of a Boop submission currently:

JSON:
```
  { 
    "created_at": "2018-02-26T14:46:15.704Z", 
    "box_id": 64, 
    "print_id": "347"
  }
```

 Yes, "print_id" appears to be sent as a string, so to support this, both IDs can be sent as integers or strings.
 
`box_id` can also be a Box's UUID - this should be the standard in the future. e.g.:

```
  { 
    "created_at": "2018-02-26T14:46:15.704Z", 
    "box_id": '1277209b-7e87-4023-a852-617e79ae6b18', 
    "print_id": "347"
  }
```

### Returned

Nothing.  Status code should indicate success or failure, but the returned body is ignored.

## Retrieve list of available boxes

GET http://museuminabox.herokuapp.com/boxes.json

### Returned
JSON:
```
  [
    {
      "id": box_id, 
      "url": box_details_url,
      "name": "Name of the Box",
      "brain_type": "audio"  // LEGACY, used to be either "audio" or "video", currently "audio" is the only type supported
    },
    ...
  ]
```

## Retrieve box details

GET http://museuminabox.herokuapp.com/boxes/:box_id.json

`box_id` can be the Box's database ID or its UUID (for newer boxes).

## Retrieve list of prints for this box

GET http://museuminabox.herokuapp.com/boxes/:box_id/list.json

`box_id` can be the Box's database ID or its UUID (for newer boxes).
 