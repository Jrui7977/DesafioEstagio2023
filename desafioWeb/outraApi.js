
const dog_btn = document.getElementById("dog_btn");

if(dog_btn){
    dog_btn.addEventListener('click', () =>{
        getRandomDog();
    });
}
else
    console.log('a')

function getRandomDog() {
	fetch('https://random.dog/woof.json')
		.then(res => res.json())
		.then(data => {
			if(data.url.includes('.mp4')) {
				getRandomDog();
			}
			else {
				dog_result.innerHTML = `<img src=${data.url} alt="dog" />`;
			}
		});
}



const cat_result = document.getElementById('cat_result');
const dog_result = document.getElementById('dog_result');
