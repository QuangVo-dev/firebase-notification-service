importScripts('https://www.gstatic.com/firebasejs/6.2.2/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/6.2.2/firebase-messaging.js');

const firebaseConfig = {
    apiKey: "AIzaSyCFy_cJsPKNfQx02aLBRU_DqG0xr4gjgB8",
    authDomain: "quickstart-1557570824261.firebaseapp.com",
    databaseURL: "https://quickstart-1557570824261.firebaseio.com",
    projectId: "quickstart-1557570824261",
    storageBucket: "quickstart-1557570824261.appspot.com",
    messagingSenderId: "889939639834",
    appId: "1:889939639834:web:c98986ae1e7e2e1b"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging()
messaging.setBackgroundMessageHandler(payload => {
    const options = {
        body: payload.data.status
    }
    return self.registration.showNotification("Hello World", options)
})