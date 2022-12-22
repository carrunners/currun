
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

// $(function() {
//     $('button#forward').on('pointerdown', function(e) {
//     e.preventDefault()
//     $.getJSON('/forward_start',
//         function(data) {
//             console.log(data)
//     });
//     });
// $('button#forward').on('pointerup', function(e) {
//     e.preventDefault()
//     $.getJSON('/forward_stop',
//         function(data) {
//             console.log(data)
//     });
//     });
// });
// $(function() {
//     $('button#left').on('pointerdown', function(e) {
//     e.preventDefault()
//     $.getJSON('/left_start',
//         function(data) {
//             console.log(data)
//     });
//     });
//     $('button#left').on('pointerup', function(e) {
//     e.preventDefault()
//     $.getJSON('/left_stop',
//         function(data) {
//             console.log(data)
//     });
//     });
// });
// $(function() {
//     $('button#right').on('pointerdown', function(e) {
//     e.preventDefault()
//     $.getJSON('/right_start',
//         function(data) {
//             console.log(data)
//     });
//     });
//     $('button#right').on('pointerup', function(e) {
//     e.preventDefault()
//     $.getJSON('/right_stop',
//         function(data) {
//             console.log(data)
//     });
//     });
// });
// $(function() {
//     $('button#backward').on('pointerdown', function(e) {
//     e.preventDefault()
//     $.getJSON('/backward_start',
//         function(data) {
//             console.log(data)
//     });
//     });
//     $('button#backward').on('pointerup', function(e) {
//     e.preventDefault()
//     $.getJSON('/backward_stop',
//         function(data) {
//             console.log(data)
//     });
//     });
// });