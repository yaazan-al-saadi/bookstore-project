function validateOrderForm() {
    let fullName = document.forms["orderForm"]["full_name"].value;
    let email = document.forms["orderForm"]["email"].value;
    let phone = document.forms["orderForm"]["phone"].value;
    let bookTitle = document.forms["orderForm"]["book_title"].value;

    if (fullName === "" || email === "" || phone === "" || bookTitle === "") {
        alert("Please fill in all fields.");
        return false;
    }

    if (!email.includes("@")) {
        alert("Please enter a valid email.");
        return false;
    }

    return true;
}

function validateContactForm() {
    let name = document.forms["contactForm"]["name"].value;
    let email = document.forms["contactForm"]["email"].value;
    let message = document.forms["contactForm"]["message"].value;

    if (name === "" || email === "" || message === "") {
        alert("Please fill in all fields.");
        return false;
    }

    if (!email.includes("@")) {
        alert("Please enter a valid email.");
        return false;
    }

    return true;
}