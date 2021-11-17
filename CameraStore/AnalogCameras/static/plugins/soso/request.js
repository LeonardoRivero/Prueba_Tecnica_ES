function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

async function request_put(url, dataToPut) {
    var response = await fetch(url, {
        credentials: 'same-origin',
        method: 'PUT',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: dataToPut
    })
    return response
}
async function request_get(url) {
    var response = await fetch(url, {
        credentials: 'include',
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'content_type': "application/json"
        },
    })
    return response
}
async function request_post(url, dataToPost) {
    var response = await fetch(url, {
        credentials: 'same-origin',
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: dataToPost,
    })
    return response
}

async function request_delete(url) {
    var response = await fetch(url, {
        credentials: 'same-origin',
        method: 'DELETE',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    })
    return response
}

