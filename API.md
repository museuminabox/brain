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

## Retrieve list of prints for this box

GET http://museuminabox.herokuapp.com/boxes/:box_id/list.json
 
