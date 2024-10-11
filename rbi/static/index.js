
static/index.js

var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}

function calcular() {
    var num1 = Number(document.getElementById("espemed").value);
    var num2 = Number(document.getElementById("txcormetal").value);
    var num3 = Number(document.getElementById("agetk").value);
    var num4 = Number(document.getElementById("tolscad").value);
    var num5 = Number(document.getElementById("txcorclad").value);
    var num6 = Number(document.getElementById("tensaores").value);
    var num7 = Number(document.getElementById("tensaoesco").value);
    var num8 = Number(document.getElementById("eficjun").value);
    var num9 = Number(document.getElementById("tensaoad").value);
    var num10 = Number(document.getElementById("espereq").value);
    var num11 = Number(document.getElementById("presproj").value);
    var num12 = Number(document.getElementById("diametrocomp").value);


    var elemResult = document.getElementById("resultado");
    var elemResult2 = document.getElementById("resultado2");
    var elemResult3 = document.getElementById("resultado3");
    var elemResult4 = document.getElementById("resultado4");
    var elemResult6 = document.getElementById("resultado6");
    var elemResult7 = document.getElementById("resultado7");
    var elemResult8 = document.getElementById("resultado8");
    var elemResult9 = document.getElementById("resultado9");
    var elemResult10 = document.getElementById("resultado10");
    var elemResult11 = document.getElementById("resultado11");
    var elemResult12 = document.getElementById("resultado12");
    var elemResult13 = document.getElementById("resultado13");
    var elemResult14 = document.getElementById("resultado14");
    var elemResult15 = document.getElementById("resultado15");
    var elemResult16 = document.getElementById("resultado16");
    var elemResult17 = document.getElementById("resultado17");
    var elemResult18 = document.getElementById("resultado18");
    var elemResult19 = document.getElementById("resultado19");
    var elemResult20 = document.getElementById("resultado20");
    var elemResult21 = document.getElementById("resultado21");
    var elemResult22 = document.getElementById("resultado22");
    var elemResult23 = document.getElementById("resultado23");
    var elemResult24 = document.getElementById("resultado24");
    

    if (elemResult.textContent === undefined) {
       elemResult.textContent = "Art = (1-(tmin-C*age)/(tmin+CA) = " + Number(1-(num1-num2*num3)/(num1+num4)).toFixed(4) + ".";
    }
    else { // IE
       elemResult.innerText = "Art = (1-(tmin-C*age)/(tmin+CA) =" + Number(1-(num1-num2*num3)/(num1+num4)).toFixed(4) + ".";
    }
    if (elemResult2.textContent === undefined) {
      elemResult2.textContent = "Art = (Cr,bm*agetk)/trdi) = " + Number(1-(num1-num2*num3)/(num1+num4)).toFixed(4) + ".";
   }
   else { // IE
      elemResult2.innerText = "Art = (Cr,bm*agetk)/trdi) =" + Number((num2*num3)/num1).toFixed(4) + ".";
   }
   if (elemResult3.textContent === undefined) {
      elemResult3.textContent = "Art = (Cr,cm*agetk)/trdi) = " + Number(1-(num1-num2*num3)/(num1+num4)).toFixed(4) + ".";
   }
   else { // IE
      elemResult3.innerText = "Art = (Cr,cm*agetk)/trdi) =" + Number((num5*num3)/num1).toFixed(4) + ".";
   }
   if (elemResult4.textContent === undefined) {
      elemResult4.textContent = "Art = (Cr,cm*agetk+Crbm*agetk-agerc))/trdi) = " + Number((num5*num3)/num1).toFixed(4) + ".";
   }
   else { // IE
      elemResult4.innerText = "Art = (Cr,cm*agetk+Crbm*agetk-agerc))/trdi) =" + Number((num5*num3+num2*num3)/num1).toFixed(4) + ".";
   }
   if (elemResult6.textContent === undefined) {
      elemResult6.textContent = "((TS+YS)/2*E*1,1)) = " + Number(((num7+num6)*num8*1.1)/2).toFixed(4) + ".";
   }
   else { // IE
      elemResult6.innerText = "((TS+YS)/2*E*1,1)) =" + Number(((num7+num6)*num8*1.1)/2).toFixed(2) + ".";
   }
   if (elemResult7.textContent === undefined) {
      elemResult7.textContent = "S*E*MAX(tmin,tc)/(FSThin*trdi) " + Number(num9*num8*Math.max(num1,num10)/((((num7+num6)*num8*1.1)/2)*num1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult7.innerText = "S*E*MAX(tmin,tc)/(FSThin*trdi) =" + Number(num9*num8*Math.max(num1,num10)/((((num7+num6)*num8*1.1)/2)*num1)).toFixed(4) + ".";
   }
   if (elemResult8.textContent === undefined) {
      elemResult8.textContent = "alpha =" + Number(2).toFixed(4) + ".";
   }
   else { // IE
      elemResult8.innerText = "alpha =" + Number(2).toFixed(2) + ".";
   }
   if (elemResult9.textContent === undefined) {
      elemResult9.textContent = "P*D/(alpha*FS*trdi) =" + Number((num11*num12/1000)/(2*(((num7+num6)*num8*1.1)/2)*num1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult9.innerText = "P*D/(alpha*FS*trdi) =" + Number((num11*num12/1000)/(2*(((num7+num6)*num8*1.1)/2)*num1)).toFixed(4) + ".";
   }
   if (elemResult10.textContent === undefined) {
      elemResult10.textContent = "10 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult10.innerText = "10_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult11.textContent === undefined) {
      elemResult11.textContent = "11 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult11.innerText = "11_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult12.textContent === undefined) {
      elemResult12.textContent = "12 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult12.innerText = "12_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult13.textContent === undefined) {
      elemResult13.textContent = "13 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult13.innerText = "13_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult14.textContent === undefined) {
      elemResult14.textContent = "14 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult14.innerText = "14_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult15.textContent === undefined) {
      elemResult15.textContent = "15 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult15.innerText = "15_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult16.textContent === undefined) {
      elemResult16.textContent = "16 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult16.innerText = "16_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult17.textContent === undefined) {
      elemResult17.textContent = "17 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult17.innerText = "17_1=" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult18.textContent === undefined) {
      elemResult18.textContent = "18 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult18.innerText = "18_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult19.textContent === undefined) {
      elemResult19.textContent = "19 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult19.innerText = "19_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult20.textContent === undefined) {
      elemResult20.textContent = "20 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult20.innerText = "20_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult21.textContent === undefined) {
      elemResult21.textContent = "21 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult21.innerText = "21_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult22.textContent === undefined) {
      elemResult22.textContent = "22 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult22.innerText = "22_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult23.textContent === undefined) {
      elemResult23.textContent = "23 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult23.innerText = "23_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   if (elemResult24.textContent === undefined) {
      elemResult24.textContent = "24 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
   else { // IE
      elemResult24.innerText = "24_1 =" + Number((0.1*0.1)).toFixed(4) + ".";
   }
}


