// var slides = document.querySelectorAll("#slides > img");
// var prev = document.getElementById("prev");
// var next = document.getElementById("next");
// var current = 0;

// showSlides(current);
// prev.onclick = prevSlide;
// next.onclick = nextSlide;

// function showSlides(n) {
//   for (let i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   slides[n].style.display = "block";
// }

// function prevSlide() {
//   if (current > 0) current -= 1;
//   else
//     current = slides.length - 1;
//     showSlides(current);
// }

// function nextSlide() {
//   if (current < slides.length - 1) current += 1;
//   else
//     current = 0;
//     showSlides(current);  
// }

//자동 이미지 출력 

let picture = ["{% static 'board/images/django.jpg' %}","{% static 'board/images/django2.jpg' %}","{% static 'board/images/django3.jpg' %}"];
let msg_idx = 0;

showPicture(); //호출

function showPicture(){
   let pic =  document.getElementById("intro_img");
   pic.src = picture[msg_idx];
   msg_idx++;
      if(msg_idx === picture.length){
      msg_idx = 0;
       }
    setTimeout(showPicture,2000); // 콜백함수(함수의 매개변수로 함수를 설정)
     }

     setInterval(function(){
        const now = new Date();
        let watch = now.toLocaleTimeString();
        document.querySelector("#display").innerHTML = watch;
     },1000)