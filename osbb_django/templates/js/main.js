$(document).ready(function(){$(".embed-responsive > a").click(function(){var modalTarget=$(this).attr("href");var videoSRC=$(this).attr("data-video"),videoSRCauto=videoSRC+"?modestbranding=1&rel=0&controls=0&showinfo=0&html5=1&autoplay=1";$(modalTarget+' iframe').attr('src',videoSRCauto);$(modalTarget+' button.close').click(function(){$(modalTarget+' iframe').attr('src',videoSRC);});});$(".nav-text").click(function(){if(!$(this).hasClass("activenav")){$("a.nav-text").removeClass("activenav");$(".navbar-nav li").removeClass("activeli");$(this).addClass("activenav");$(this).parent("li").addClass("activeli");}});$('.myCarousel').slick({responsive:[{breakpoint:768,settings:{arrows:false,slidesToShow:1}},{breakpoint:480,settings:{arrows:false,slidesToShow:1}}]});$('.video-desc').slick({slidesToShow:1,slidesToScroll:1,arrows:false,fade:true,asNavFor:'.video-youtube',adaptiveHeight:true});$('.video-youtube').slick({centerMode:true,centerPadding:'0',slidesToScroll:1,asNavFor:'.video-desc',focusOnSelect:true,slidesToShow:3,responsive:[{breakpoint:768,settings:{arrows:false,centerMode:true,centerPadding:'40px',slidesToShow:2}},{breakpoint:480,settings:{arrows:false,centerMode:true,centerPadding:'40px',slidesToShow:1}}]});$('a[href*="#"]').not('[href="#"]').not('[href="#0"]').click(function(event){if(location.pathname.replace(/^\//,'')==this.pathname.replace(/^\//,'')&&location.hostname==this.hostname){var target=$(this.hash);target=target.length?target:$('[name='+this.hash.slice(1)+']');if(target.length){event.preventDefault();$('html, body').animate({scrollTop:target.offset().top},1000,function(){var $target=$(target);$target.focus();if($target.is(":focus")){return false;}else{$target.attr('tabindex','-1');$target.focus();};});}}});$("#ordercall").submit(function(e){e.preventDefault();var form=$("#ordercall");var error=false;if(!error){var data=form.serialize();$.ajax({type:'POST',url:'feedback.php',dataType:'json',data:data,success:function(data){if(data['error']){alert(data['error']);}else{$('#callBack').modal("hide");$('#thanks').modal("show");var form1_input1=form.find("input");form1_input1.value="";}},error:function(xhr,ajaxOptions,thrownError){alert(xhr.status);alert(thrownError);}});}
return false;});});