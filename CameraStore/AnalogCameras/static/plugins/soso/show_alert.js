async function show_response(response) {
    var responseAsJson = await response.json();
    var message = responseAsJson.message;
    if (response.status == 200) {
        var result = await show_message("success", message)
        return { result, responseAsJson }

    } else {
        const message_clg = `An error has occured here request_post: ${response.status}`;
        var result = await show_message("error", message)
        return { result, responseAsJson }

    }
}

async function show_message(level_message, message) {
    var result = Swal.fire({
        title: level_message,
        text: message,
        icon: level_message,
    })
    return result
}

function showloading(message) {
    Swal.fire({
        title: 'Please Wait !',
        html: message, // add html attribute if you want or remove
        allowOutsideClick: false,
        onBeforeOpen: function() {
            Swal.showLoading()
        },
    });
}