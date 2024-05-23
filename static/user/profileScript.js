function showAddAddressModal() {
  const modal = document.getElementById("addAddressModal");
  modal.style.display = "block";
  isFormVisible = true;
}

function closeAddAddressModal() {
  const modal = document.getElementById("addAddressModal");
  modal.style.display = "none";
  isFormVisible = false;
}

function showProfileDetails() {
  hideAllSections();
  document.getElementById("profileDetails").style.display = "block";
  setActiveLink(0);
}

function showOrderDetails() {
  hideAllSections();
  document.getElementById("orderDetails").style.display = "block";
  setActiveLink(1);
}

function showAddressBook() {
  hideAllSections();
  document.getElementById("addressBook").style.display = "block";
  setActiveLink(2);
}

function hideAllSections() {
  document.getElementById("orderDetails").style.display = "none";
  document.getElementById("profileDetails").style.display = "none";
  document.getElementById("addressBook").style.display = "none";
}

function setActiveLink(index) {
  document.querySelector(".list-group-item.active").classList.remove("active");
  document.querySelectorAll(".list-group-item")[index].classList.add("active");
}

showProfileDetails();
