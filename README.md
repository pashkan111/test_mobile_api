# test_mobile_api

1. To start service, run the command: docker-compose up -d --build

### Routes
1. Return all shops the request user has access:
    _GET api/shops?phone=****_
    
2. Route allows you visit shop if you havw an access:
    _POST api/visit?phone=****_<br/>
    #### data: <br/>
    id:int,<br/>
    latitude: float <br/>
    longitude: float <br/>
    
