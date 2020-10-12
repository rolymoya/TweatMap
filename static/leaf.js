var corner1 = L.latLng(84.938342, -200),
corner2 = L.latLng(-84.953827, 200),
bounds = L.latLngBounds(corner1, corner2)

var mymap = L.map('mapid', {maxBoundsViscosity : 1}).setView([39.50, -98.35], 5).setMinZoom(2.5).setMaxBounds(bounds);

L.tileLayer('https://api.mapbox.com/styles/v1/{username}/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    username:'rolymoya',
    id: 'ckg5ny9s33uxz19s2vbh4ic7g',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1Ijoicm9seW1veWEiLCJhIjoiY2tnNWUzbGx2MGV5czJwcXRybGkyMXM4byJ9.9BTe1rH0wWEXdZ8x-rkadQ'
}).addTo(mymap);

var source = new EventSource('/topic/twitterdata');

source.addEventListener('message', function(e){
    obj = JSON.parse(e.data);
    console.log(obj);
    lat = obj.place.bounding_box.coordinates[0][0][1];
    long = obj.place.bounding_box.coordinates[0][0][0];
    profile_image = obj.user.profile_image_url;
    username = obj.user.name;
    screen_name = obj.user.screen_name;
    tweet = obj.text;

    marker = L.marker([lat,long],).addTo(mymap).bindPopup('<div><img src="'+ profile_image + '" alt="Twitter User Profile Picture" style="border-radius:50%"> <b>'+ username + '</b> <b> @' + screen_name + '</b><br>' + tweet + '</div>');
}, false);