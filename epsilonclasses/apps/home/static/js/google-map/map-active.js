{
  var uluru = {lat: 25.278222 ,lng: 82.992472};

  var map = new google.maps.Map(document.getElementById('googleMap'), {
    zoom: 17,
    center: uluru
  });

}
var marker = new google.maps.Marker({
  position: uluru,
  map: map,

});

