function deleteConfirmation(id){
    const response = confirm("Estas seguro?")

    if(response){
        window.location.href = "/posts/delete/"+id
    }
}