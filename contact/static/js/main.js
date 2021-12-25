// Навигация
const about = document.getElementById('about');
	  contact = document.getElementById('contact');
	  contactBtn = document.querySelector('.main__header-btn');
	  contactHeaderBtn = document.querySelector('#headerContact');
	  aboutHeaderBtn = document.querySelector('#headerAbout');


function scrollToContact() {
	contact.scrollIntoView({block: "center", behavior: "smooth"});
}


contactBtn.addEventListener('click', scrollToContact);
contactHeaderBtn.addEventListener('click', scrollToContact);


function scrollToAbout() {
	about.scrollIntoView({block: "center", behavior: "smooth"});
}


aboutHeaderBtn.addEventListener('click', scrollToAbout);


// Формы
const tForm = document.querySelector('#tourist-form'),
	  eForm = document.querySelector('#employer-form'),
	  tBtn = document.querySelector('.kind-left'),
	  eBtn = document.querySelector('.kind-right')

tBtn.addEventListener('click', () => {
	if (eBtn.classList.contains('active')) {
		eBtn.classList.remove('active')
	}
	tBtn.classList.add('active')

	if (eForm.classList.contains('form-active')) {
		eForm.classList.remove('form-active')
	}
	tForm.classList.add('form-active')
})

eBtn.addEventListener('click', () => {
	if (tBtn.classList.contains('active')) {
		tBtn.classList.remove('active')
	}
	eBtn.classList.add('active')

	if (tForm.classList.contains('form-active')) {
		tForm.classList.remove('form-active')
	}
	eForm.classList.add('form-active')
})

// Коллабы
const collabs = document.querySelectorAll(".main__collab-body ul > li");

function closeDetails(collab, icon, detail) {
	collab.classList.remove('collab-active');
	icon.classList.remove('bi-chevron-down');
	icon.classList.add('bi-chevron-right');
	detail.style.setProperty('display', 'none');
}

for (let collab of collabs) {
	collab.addEventListener('click', () => {
		icon = collab.querySelector('i');
		detail = collab.querySelector('.main__collab-detail');
		for (let acollab of collabs) {
			aicon = acollab.querySelector('i');
			adetail = acollab.querySelector('.main__collab-detail');
			if (aicon.classList.contains('bi-chevron-down') && (icon != aicon)) {
				closeDetails(acollab, aicon, adetail);
			}
		}
		if (icon.classList.contains('bi-chevron-right')) {
			collab.classList.add('collab-active');
			icon.classList.remove('bi-chevron-right');
			icon.classList.add('bi-chevron-down');
			detail.style.setProperty('display', 'block');
		} else {
			closeDetails(collab, icon, detail);
		}
	})
}
