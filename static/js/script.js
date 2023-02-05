function get_userID(userID)
{
    console.log(userID)

    console.log(userID.firstElementChild)
    // document.getElementById('the_userID').textContent = x.textContent;
    userID = userID.firstElementChild.textContent
    document.getElementById('the_userID').textContent = userID
    document.getElementById('the_userID_field').value = userID
    return userID
}

function getvalue(){
    var user = document.getElementById('the_userID_field').value;
    console.log(user)
    if (user == ""){
      console.log("x is Empty")
      document.getElementById('userID_in_modal').innerText = "No user selected";
    }else{
    document.getElementById('userID_in_modal').innerText = `Are you sure that you want to delete user: ${user}`
    }
  }