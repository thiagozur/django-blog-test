const popupbtn = document.getElementsByClassName('popupbtn');
    const popup = document.getElementsByClassName('popup-wrapper');
    const slugs = document.getElementsByClassName('slugsaver');
    const deleters = document.getElementsByClassName('deleter');
    const noers = document.getElementsByClassName('noer');
    const notpops = document.getElementsByClassName('notpop')

    Array.from(popupbtn).forEach(function (element, index) {
        element.addEventListener('click', () => {
            popup[index].classList.toggle('hideP');
            Array.from(notpops).forEach(function (element) {
                element.classList.toggle('bl')
            })
        })
    })

    Array.from(deleters).forEach(function (element, index) {
        element.addEventListener('click', () => {
            const path = '/blog/delpost/' + slugs[index].innerHTML
            location.assign(path)
        })
    })

    Array.from(noers).forEach(function (element, index) {
        element.addEventListener('click', () => {
            popup[index].classList.toggle('hideP')
            Array.from(notpops).forEach(function (element, index) {
                element.classList.toggle('bl')
            })
        })
    })

    Array.from(popup).forEach(function (element, index) {
        element.addEventListener('click', (e) => {
            if(e.target.className === 'popup-wrapper') {
                element.classList.toggle('hideP')
            }
        })
    })