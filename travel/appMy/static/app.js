function bannerSwitcher() {
    next = $('.sec-1-input').filter(':checked').next('.sec-1-input');
    if (next.length) next.prop('checked', true);
    else $('.sec-1-input').first().prop('checked', true);
  }

  var bannerTimer = setInterval(bannerSwitcher, 5000);

  $('nav .controls label').click(function() {
    clearInterval(bannerTimer);
    bannerTimer = setInterval(bannerSwitcher, 5000)
  });

  $(window).scroll(function () { 
    

    $('nav').toggleClass('scrolled',$(this).scrollTop()>50);




});



window.onload = function() {
  // animasyon kodunuz buraya


  ScrollReveal({ 
    reset: false,
    distance:"60px",
    duration:1000,
    delay:400,
   });
  
   ScrollReveal().reveal('.image-contents',{origin:"left" });
   ScrollReveal().reveal('.map',{origin:"right" });
   ScrollReveal().reveal('.contess',{origin:"bottom" });
   ScrollReveal().reveal('.const',{origin:"bottom" });
   ScrollReveal().reveal('.main-caption',{origin:"left" });
   ScrollReveal().reveal('.more-info',{origin:"top" });

}




// $(document).ready(function() {
//   var isFirstLoad = true; // İlk yükleme için bir bayrak oluşturun

//   $(window).on('beforeunload', function() {
//     isFirstLoad = false; // Sayfa yeniden yüklenirken bayrağı güncelleyin
//   });

//   if (performance.navigation.type !== 1 && isFirstLoad) {
//     // Sayfa yenilenmediyse ve ilk yükleme sırasında animasyonu çalıştır
//     startAnimation();
//   }

//   function startAnimation() {
//     $(".loginleft").css({
//       "transform": "translateX(-200%)",
//       "transition": "all 2s ease"
//     });
//     $(".loginright").css({
//       "transform": "translateX(200%)",
//       "transition": "all 2s ease"
//     });

//     setTimeout(function() {
//       $(".loginpage").css("display", "none");
//     }, 2000); // Süreyi istediğiniz gibi ayarlayın
    
//     // Diğer sayfa içeriğini burada görüntüleyin
//   }
// });
// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
// 	container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });