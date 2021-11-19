import { morseRegex } from './morseDict.js'

const socket = io('/morse');

// ----------------------------------------------------------------------------

// User interface elements filled after loading:
let userHelp = null;
let morseContainer = null;
let morseHelpButton = null;
let userInput = null;
let morseMonitor = null;
let userHelperText = null;

// ----------------------------------------------------------------------------

function configSocket() {

    socket.on('connect', _ => socket.emit('morseEvt', {data: "socket_connected"}) );

    socket.on('morseEvtResponse', (msg, callBack) => {
        renderDecodedResponse(msg.data);
        if (callBack) callBack();
    });
}

// ----------------------------------------------------------------------------

function renderDecodedResponse(msg) {
    morseMonitor.append(msg);

    const scrollVal = morseMonitor.scrollHeight || 0;
    morseMonitor.scrollTop = scrollVal;
}

// ----------------------------------------------------------------------------

function sendUserData(data) {
    morseMonitor.innerHTML += `<br/>[${data}] : `;
    socket.emit('morseEvt', {data});
}

// ----------------------------------------------------------------------------

function displayFlexElement(element, show) {
    element.style.display = show ? 'flex' : 'none';
}

// ----------------------------------------------------------------------------

function handleUserInput(event) {
    const typed = (event.target || {}).value || '';

    const matches = typed.match(morseRegex);

    if(!matches) {
        setUserHelperText('Código inválido!', 'tomato');
        return;
    }
    setUserHelperText('Continue...', 'seagreen');

    if (event.keyCode === 13) {
        sendUserData(typed);
        event.target.value = '';
    }
}

// ----------------------------------------------------------------------------

function setUserHelperText(txt, color) {
    userHelperText.textContent = txt;
    userHelperText.style.color = color;
}

// ----------------------------------------------------------------------------

function startWebSocket() {

}

// ----------------------------------------------------------------------------

function config() {

    configSocket();

    userHelp = document.getElementById('morse-user-help');
    morseContainer = document.getElementById('morse-container');
    morseHelpButton = document.getElementById('morse-help-button');
    userInput = document.getElementById('morse-user-input');
    userHelperText = document.getElementById('morse-user-input-message');
    morseMonitor = document.getElementById('morse-monitor');

    morseHelpButton.addEventListener('click',  _ =>
        displayFlexElement(userHelp, true)
    );

    userHelp.addEventListener('click', _ =>
        displayFlexElement(userHelp, false)
    );

    userInput.addEventListener('keyup', handleUserInput);

    if(userInput) userInput.focus();
}


window.onload = _ => config();
