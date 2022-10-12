const panels = document.querySelectorAll(".panel")

panels.forEach(panel=>{
    removeActiveClasses()
    panel.addEventListener('click', () => {
        removeActiveClasses()
        panel.classList.add('active')
    })
})

function removeActiveClasses(){
    panels.forEach(panel => {
        panel.classList.remove('active')
    })
}