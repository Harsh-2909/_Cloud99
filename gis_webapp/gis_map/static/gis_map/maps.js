const convertingToRadians = (degrees) => {
    return degrees * (Math.PI / 180);
  };
  
  // Actual Calculation for finding the feasible location
  const x1 = 15.712950725807477;
  const y1 = 81.48834228515625;
  const x2 = 15.294782590260944;
  const y2 = 82.19970703125;
  
  let arr = [];
  for (let k = 0; k < 10; k++) {
    arr.push([x1 + (k / 9) * (x2 - x1), y1 + (k * (y2 - y1)) / 9]);
  }
  // console.log(arr);
  
  const distance = [
    296139.79,
    294803.91,
    293729.61,
    292919.89,
    292377.07,
    292102.78,
    292362.59,
    292896.22,
    293697.47,
    294764.29,
  ]; // The distance from Vishakhapattanam to datum point
  let time_list = [];
  distance.forEach(function (element) {
    time_list.push(element / 72.0222);
  });
  // console.log(time_list);
  
  const velocity = [
    [85, 0.03],
    [110, 0.03],
    [130, 0.04],
    [140, 0.07],
    [150, 0.11],
    [150, 0.14],
    [150, 0.18],
    [150, 0.24],
    [145, 0.27],
    [145, 0.3],
  ]; // Total Water Current
  const displacement = [];
  for (let n = 0; n < 10; n++) {
    displacement.push(time_list[n] * velocity[n][1]);
    displacement[n] = displacement[n] * 9.231617281886954e-6;
  }
  // console.log(displacement);
  
  const m_list = [];
  for (let n = 0; n < 10; n++) {
    m_list.push(Math.tan(convertingToRadians(velocity[n][0] + 270)));
  }
  // console.log(m_list);
  for (let n = 0; n < 10; n++) {
    arr[n][0] =
      arr[n][0] - displacement[n] / Math.sqrt(1 + Math.pow(m_list[n], 2));
    arr[n][1] =
      arr[n][1] -
      m_list[n] * (displacement[n] / Math.sqrt(1 + Math.pow(m_list[n], 2)));
  }
  // console.log(arr);
  
  const radius = [];
  for (let n = 0; n < 10; n++) {
    radius.push(
      Math.sqrt(
        Math.pow(1852, 2) +
          Math.pow(0.3 * time_list[n], 2) +
          Math.pow(1852 * 0.3, 2)
      )
    );
  }
  // console.log(radius);
  
  // Plotting the points inside a map and thus creating a polygon
  var mymap = L.map("mapid").setView([x1, y1], 13);
  L.tileLayer(
    "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
    {
      attribution:
        'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 18,
      id: "mapbox/streets-v11",
      tileSize: 512,
      zoomOffset: -1,
      accessToken:
        "pk.eyJ1Ijoic291cHRpazQ1NzIiLCJhIjoiY2tkOXNrM2RxMHlmbDJybm52azM2eHMwdCJ9.xH2sbKlNXtAxXEG4dvxRlg",
    }
  ).addTo(mymap);
  
  // Creating the circles based on the points
  for (let n = 0; n < 10; n++) {
    L.circle([arr[n][0], arr[n][1]], {
      // color: 'red',
      fillColor: "#ed3e67",
      fillOpacity: 0.5,
      radius: radius[n] * 3,
      stroke: false
    }).addTo(mymap);
    L.circle([arr[n][0], arr[n][1]], {
      color: 'red',
      fillColor: "#f03",
      fillOpacity: 0.5,
      radius: radius[n],
      stroke: false
    }).addTo(mymap);
  }
  
  // Creating the Polyline
  // var polyline = L.polyline(arr, {color: 'red'}).addTo(mymap);
  // // zoom the map to the polyline
  // mymap.fitBounds(polyline.getBounds());
  
  // Creating the PolyGone
  // const polyPoints = [[15.71181630638612, 81.4884415339953], [15.69368753553298, 81.47750367089544], [15.647317196289055, 81.55607147966352], [15.600784611203661, 81.63454312748541], [15.553799999769417, 81.71254695481029], [15.506974591902777, 81.79003646965961], [15.459956596285439, 81.86811050422611], [15.412737096187731, 81.94584609742401], [15.365132164373712, 82.02291953487587], [15.317330092572012, 82.10142859112081], [15.270176857220894, 82.17949905052181], [15.288281310828193, 82.19042224198684], [15.729945077239261, 81.49937939709515], [15.68352750211967, 81.57791870643844], [15.636957040907244, 81.65636750197237], [15.589943946803501, 81.7343541444841], [15.543099476217469, 81.81183215797921], [15.496071857728724, 81.88990038665568], [15.44886147234124, 81.96764147914823], [15.401275279638721, 82.04472622270781], [15.353501390650083, 82.12325228284966], [15.306385764435491, 82.20134543345186], [15.71181630638612, 81.4884415339953]]; 
  // var polygon = L.polygon(polyPoints, {color: 'green', fillColor: '#f03'}).addTo(mymap);
  
  // Creating the Circles
  // for(let i=0; i<lats.length; i++){
  //     var circle = L.circle([lats[i], longs[i]], {
  //             color: 'red',
  //             fillColor: '#f03',
  //             fillOpacity: 0.5,
  //             radius: radius[i]
  //         }).addTo(mymap);
  //     var circle = L.circle([lats[i], longs[i]], {
  //             color: 'blue',
  //             fillColor: '#346eeb',
  //             fillOpacity: 0.5,
  //             radius: radius[i]/2
  //         }).addTo(mymap);
  //  }
  
  const subButton = document.querySelector(".but");
  subButton.addEventListener("click", function () {
    let lat = Number(document.querySelector("#lat").value);
    let long = Number(document.querySelector("#long").value);
    L.circle([lat, long], {
      color: "red",
      fillColor: "#f03",
      fillOpacity: 0.5,
      radius: 1852,
    }).addTo(mymap);
  });
  