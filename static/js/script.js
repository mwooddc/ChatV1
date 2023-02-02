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