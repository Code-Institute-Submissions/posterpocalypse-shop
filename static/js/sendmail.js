// Send mail using jsdeliver on the contacts form

function sendMail(contactForm) {
    emailjs.send("outlook", "joe", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "query": contactForm.query.value
    })
        .then(
            function (response) {
                console.log("SUCCESS", response);
            },
            function (error) {
                console.log("FAILED", error);
            }
        );
    return false;  // To block from loading a new page
}