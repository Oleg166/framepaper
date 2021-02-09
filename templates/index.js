'use strict';

let el = document.getElementById('dwer');
el.addEventListener('click', foo1, false);
function foo1(e) {
    let el1 = document.getElementById('first_name');
    let el2 = document.getElementById('telephone');
    let el3 = document.getElementById('email');

    let regexp1 = /[a-z]+\D/i;
    let regexp2 = /\+\d\(\d{3}\)\d{3}\-\d{4}/;
    let regexp3 = /^([a-z0-9_\.-]+)@([a-z0-9_\.-]+)\.([a-z\.]{2,6})$/;

    let arr = [el1, el2, el3];
    let arrregexp =[regexp1, regexp2, regexp3]


    if (regexp1.test(el1.value) & regexp2.test(el2.value) & regexp3.test(el3.value)) {
        alert("данные введены верно, данные отправлены");
    }
    else {
        arr.forEach(function(item, i, arr) {
            if (arrregexp[i].test(item.value) != true) {
                item.style.borderColor = "red";
            }
            else {
                item.style.borderColor = "green";
            }
          });
        alert("данные введены неверно, поля с с ошибками выделены красным");
        e.preventDefault();
        };    
};


