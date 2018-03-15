# Cloud API

These are the calls the box expects to be able to call in the cloud service, in order to administer the box.

## Record Boop Start

POST https://museuminabox.herokuapp.com/boopstart at the start of the Boop

NO LONGER WORKING: POST https://museuminabox.herokuapp.com/boops This is the old pre-v1 API to record (the start of) a Boop

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
  "box_id": "1277209b-7e87-4023-a852-617e79ae6b18", 
  "print_id": "347"
}
```

### Success response

200 status code.

Returns the ID of the Boop that was created.

```
{
  "boop_id": 12345
}
```

### Error reponse 

400 status code (for example).

JSON returned will be like:

```
{
  "success": false,
  "errors": [
    "Something went wrong",
    "And here's another error message"
  ]
}
```

## Record Boop End

POST https://museuminabox.herokuapp.com/boopend at the end of the Boop

### Submits

JSON:
```
{ 
  "created_at": "2018-02-26T14:46:15.704Z", 
  "boop_id": 12345
}
```

### Success response

200 status code.

Returns the ID of the Boop that was updated.

```
{
  "boop_id": 12345
}
```

### Error reponse

400 status code (for example).

JSON returned will be like:

```
{
  "success": false,
  "errors": [
    "Something went wrong",
    "And here's another error message"
  ]
}
```


## Create box by UUID

POST http://museuminabox.herokuapp.com/boxes.json

### Submits

* UUID for the box to be created, as parameter `id`.
* The Hardware ID, as entered by the user. A string as parameter `hardware_id`.
* The box's exterior description. A string as parameter `exterior`.

### Success response

200 status code.

JSON of box details for the newly created box, as would be returned by the Retrieve box details API.

### Error response

400 status code (for example).

JSON returned will be like:

```
{
  "success": false,
  "errors": [
    "Something went wrong",
    "And here's another error message"
  ]
}
```
 
## Retrieve box details

GET http://museuminabox.herokuapp.com/boxes/:box_id.json

`box_id` can be the Box's database ID or its UUID (for newer boxes).

The JSON response will be something like:

```
{
  "id": "8e12b719-3c76-4a6a-9465-1087697acc61",
  "hardware_id": "0001",
  "exterior": "Shiny yellow plastic",
  "created_at": "2018-02-22T12:00:00Z",
  "updated_at": "2018-02-22T12:00:00Z",
  "brain_type": "audio",
  "private": True
}
```

## Retrieve list of prints for this box

GET http://museuminabox.herokuapp.com/boxes/:box_id/list.json

`box_id` can be the Box's database ID or its UUID (for newer boxes).
 
```
[
  {
    "id": 12,
    "url": "https://museuminabox.herokuapp.com/boxes/12/",
    "brain_type": "audio",
    "image_url": "https://museuminabox.s3.amazonaws.com/prints/images/95e5e0bd-a724-4ba2-8004-a2abb92896a5.jpg",
    "brain_filename_audio": "b1bd2c2c-ce86-4360-a195-60a40353ac72.wav",
    "brain_url_audio": "https://museuminabox.s3.amazonaws.com/prints/audio/b1bd2c2c-ce86-4360-a195-60a40353ac72.wav"
   },
   {
    "id": "8e12b719-3c76-4a6a-9465-1087697acc61",
    "url": "https://museuminabox.herokuapp.com/boxes/34/",
    "brain_type": "audio",
    "image_url": "https://museuminabox.s3.amazonaws.com/prints/images/95e5e0bd-a724-4ba2-8004-a2abb92896a5.jpg",
    "brain_filename_audio": "b1bd2c2c-ce86-4360-a195-60a40353ac72.wav",
    "brain_url_audio": "https://museuminabox.s3.amazonaws.com/prints/audio/b1bd2c2c-ce86-4360-a195-60a40353ac72.wav"
  },
]
```


## Retrieve list of available boxes

DEPRECATED.  Used in the initial brain bootstrapping workflow, now superseded by the Create Box by UUID workflow.

GET http://museuminabox.herokuapp.com/boxes.json

### Returned

JSON:
```
[
  {
    "id": box_id, 
    "hardware_id": "The box hardware ID",
    "url": box_details_url,
    "name": "Name of the Box",
    "brain_type": "audio"  // LEGACY, used to be either "audio" or "video", currently "audio" is the only type supported
  },
  ...
]
```

`box_id` will be a UUID for boxes that have them, otherwise the internal numeric database ID.
