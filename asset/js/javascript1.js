var slideIndex = 1;
Slideshow(slideIndex);
var timer = setInterval(autoplay, 3000);

function autoplay() {
    slideIndex += 1;
    Slideshow(slideIndex);
}

function plusSlides(n) {
    Slideshow(slideIndex += n);
    resetTimer();
}

function currentSlide(n) {
    Slideshow(slideIndex = n);
    resetTimer();
}

function resetTimer() {
    clearInterval(timer);
    timer = setInterval(autoplay, 3000);
}

function Slideshow(n) {
    var i;
    var slides = document.getElementsByClassName("slide");
    var controlBtns = document.getElementsByClassName("control-btn");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < controlBtns.length; i++) {
        controlBtns[i].className = controlBtns[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    controlBtns[slideIndex - 1].className += " active";
}
            

              var modal = document.getElementById('id01');
              

              window.onclick = function(event) {
                  if (event.target == modal) {
                      modal.style.display = "none";
                  }
              }
              
                function openNav() {
                  document.getElementById("myNav").style.height = "100%";
                  document.getElementById("main").style.marginLeft = "250px";
                  document.getElementById("main").style.backgroundColor = "rgba(0, 0, 0, 0.726);";
                }
        
            /* Close */
                function closeNav() {
                  document.getElementById("myNav").style.height = "0%";
                  document.getElementById("main").style.marginLeft = "0";
                  document.getElementById("main").style.backgroundColor = "none";
                }
              
                window.onscroll = function() {scrollFunction()};
        
                function scrollFunction() {
                  if (document.body.scrollTop>200 || document.documentElement.scrollTop>200) {
                    document.getElementById("navbar").style.top = "-100px";
                  } else {
                    document.getElementById("navbar").style.top = "0";
                  }
                }
        

                var num_jia = document.getElementById("num-jia");
        var num_jian = document.getElementById("num-jian");
        var input_num = document.getElementById("input-num");

        num_jia.onclick = function() {

            input_num.value = parseInt(input_num.value) + 1;
        }

        num_jian.onclick = function() {

            if(input_num.value <= 0) {
                input_num.value = 0;
            } else {

                input_num.value = parseInt(input_num.value) - 1;
            }

        }
              
                