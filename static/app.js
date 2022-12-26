
const joistikContainer = document.querySelector('.joystik__container');

joistikContainer.addEventListener("pointerdown", e => {
    switch(e.target.id) {
        case 'forward': 
            fetch('/forward_start');
            break;
        case 'backward': {
            fetch('/backward_start');
            break;
        }
        case 'right': {
            fetch('/right_start');
            break;
        }
        case 'left': {
            fetch('/left_start');
            break;
        }
    }    
})

joistikContainer.addEventListener("pointerup", e => {
    switch(e.target.id) {
        case 'forward': {
            fetch('/forward_stop');
            break;
        }
        case 'backward': {
            fetch('/backward_stop');
            break;
        }
        case 'right': {
            fetch('/right_stop');
            break;
        }
        case 'left': {
            fetch('/left_stop');
            break;
        }
    }   
})

window.addEventListener("unload", e => {
    fetch("/exit")
})