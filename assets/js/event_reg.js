const memberContainer = document.querySelectorAll(".memberContainer");
const amount =document.getElementsByClassName("amount")






// count the number from the dropdown
var e = document.getElementById("Totalmembers");
function numberSelected() {
  var strUser = e.options[e.selectedIndex].value;
  containerSelected(strUser);
  if(strUser!="0"){
    document.getElementById("costid").value = 500;
  }
 else{
  document.getElementById("costid").value = 500*strUser;
 }
 document.getElementById("costid").readOnly = true
}

// turn display form none=>block
function containerSelected(num) {
  for (var i = 0; i < num; i++) {
    memberContainer[i].style.display = "block";
  }
  for (var i = num; i < 5; i++) {
    memberContainer[i].style.display = "none";
  }
}
e.onchange = numberSelected;



numberSelected();

console.log(amount)


var totalMembers=e.options[e.selectedIndex].value;

