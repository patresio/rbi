
static/index.js

var tab46 = 
{
"Planilha1":[
 {
  "Column1": "CoTHINp1",
  "E": 0.33,
  "D": 0.4,
  "C": 0.5,
  "B": 0.7,
  "A": 0.9
 },
 {
  "Column1": "CoTHINp2",
  "E": 0.33,
  "D": 0.33,
  "C": 0.3,
  "B": 0.2,
  "A": 0.09
 },
 {
  "Column1": "CoTHINp3",
  "E": 0.33,
  "D": 0.27,
  "C": 0.2,
  "B": 0.1,
  "A": 0.01
 }
]
};

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
    var num13 = (document.getElementById("pontoinje").value);
    var num14 = (document.getElementById("deadleg").value);
    var num15 = (document.getElementById("tipoconst").value);
    var num16 = (document.getElementById("manutapi653").value);
    var num17 = (document.getElementById("recalqapi653").value);    
    var num18 = (document.getElementById("monitora").value);
          
    var elemResult = document.getElementById("resultado");
    var elemResult2 = document.getElementById("resultado2");
    var elemResult3 = document.getElementById("resultado3");
    var elemResult4 = document.getElementById("resultado4");
    var elemResult5 = document.getElementById("resultado5");
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
    var elemResult25 = document.getElementById("resultado25");
    var elemResult26 = document.getElementById("resultado26");
    var elemResult27 = document.getElementById("resultado27");
    

    if (elemResult.textContent === undefined) {
       elemResult.textContent = "Art = (1-(tmin-C*age)/(tmin+CA) = " + Number(1-(num1-num2*num3)/(num1+num4)).toFixed(4);
    }
    else { // IE
       elemResult.innerText = "Art = (1-(tmin-C*age)/(tmin+CA) =" + Number(1-(num1-num2*num3)/(num1+num4)).toFixed(4);
    }
    if (elemResult2.textContent === undefined) {
      elemResult2.textContent = "Art = (Cr,bm*agetk)/trdi) = " + Number(1-(num1-num2*num3)/(num1+num4)).toFixed(4);
   }
   else { // IE
      elemResult2.innerText = "Art = (Cr,bm*agetk)/trdi) =" + Number((num2*num3)/num1).toFixed(4);
   }
   if (elemResult3.textContent === undefined) {
      elemResult3.textContent = "Art = (Cr,cm*agetk)/trdi) = " + Number(1-(num1-num2*num3)/(num1+num4)).toFixed(4);
   }
   else { // IE
      elemResult3.innerText = "Art = (Cr,cm*agetk)/trdi) =" + Number((num5*num3)/num1).toFixed(4);
   }
   if (elemResult4.textContent === undefined) {
      elemResult4.textContent = "Art = (Cr,cm*agetk+Crbm*agetk-agerc))/trdi) = " + Number((num5*num3)/num1).toFixed(4);
   }
   else { // IE
      elemResult4.innerText = "Art = (Cr,cm*agetk+Crbm*agetk-agerc))/trdi) =" + Number((num5*num3+num2*num3)/num1).toFixed(4);
   }
   if (elemResult5.textContent === undefined) {
      elemResult5.textContent = "5= " + Number((num5*num3)/num1).toFixed(4);
   }
   else { // IE
      elemResult5.innerText = "5_1 = (Cr,cm*agetk+Crbm*agetk-agerc))/trdi) =" + Number((num5*num3+num2*num3)/num1).toFixed(4);
   }
   if (elemResult6.textContent === undefined) {
      elemResult6.textContent = "((TS+YS)/2*E*1,1)) = " + Number(((num7+num6)*num8*1.1)/2).toFixed(4);
   }
   else { // IE
      elemResult6.innerText = "((TS+YS)/2*E*1,1)) =" + Number(((num7+num6)*num8*1.1)/2).toFixed(2);
   }
   if (elemResult7.textContent === undefined) {
      elemResult7.textContent = "S*E*MAX(tmin,tc)/(FSThin*trdi) " + Number(num9*num8*Math.max(num1,num10)/((((num7+num6)*num8*1.1)/2)*num1)).toFixed(4);
   }
   else { // IE
      elemResult7.innerText = "S*E*MAX(tmin,tc)/(FSThin*trdi) =" + Number(num9*num8*Math.max(num1,num10)/((((num7+num6)*num8*1.1)/2)*num1)).toFixed(4);
   }
   if (elemResult8.textContent === undefined) {
      
      


      
      elemResult8.textContent = "alpha =" + JSON.parse(tab46);



      

   }
   else { // IE
      elemResult8.innerText = "alpha =" + Number(2).toFixed(2);
   }
   if (elemResult9.textContent === undefined) {
      elemResult9.textContent = "P*D/(alpha*FS*trdi) =" + Number((num11*num12/1000)/(2*(((num7+num6)*num8*1.1)/2)*num1)).toFixed(4);
   }
   else { // IE
      elemResult9.innerText = "P*D/(alpha*FS*trdi) =" + Number((num11*num12/1000)/(2*(((num7+num6)*num8*1.1)/2)*num1)).toFixed(4);
   }
   if (elemResult10.textContent === undefined) {
      elemResult10.textContent = + Number((0.5*0.9**0)*(0.7**1)*(0.5**0)*(0.4**0)).toFixed(4);
      var resultado10 = ((0.5*0.9**0)*(0.7**1)*(0.5**0)*(0.4**0));
   }
   else { // IE
      elemResult10.innerText = + Number((0.5*0.9**0)*(0.7**1)*(0.5**0)*(0.4**0)).toFixed(4);
      var resultado10 = ((0.5*0.9**0)*(0.7**1)*(0.5**0)*(0.4**0));
   }
   if (elemResult11.textContent === undefined) {
      elemResult11.textContent = "11 =" + Number((0.3*0.09**0)*(0.2**1)*(0.3**0)*(0.33**0)).toFixed(4);
      var resultado11 = ((0.3*0.09**0)*(0.2**1)*(0.3**0)*(0.33**0));
   }
   else { // IE
      elemResult11.innerText = "11_1 =" + Number((0.3*0.09**0)*(0.2**1)*(0.3**0)*(0.33**0)).toFixed(4);
      var resultado11 = ((0.3*0.09**0)*(0.2**1)*(0.3**0)*(0.33**0));
   }
   if (elemResult12.textContent === undefined) {
      elemResult12.textContent = "12 =" + Number((0.2*0.01**0)*(0.1**1)*(0.2**0)*(0.27**0)).toFixed(4);
      var resultado12 = ((0.2*0.01**0)*(0.1**1)*(0.2**0)*(0.27**0));
   }
   else { // IE
      elemResult12.innerText = "12_1 =" + Number((0.2*0.01**0)*(0.1**1)*(0.2**0)*(0.27**0)).toFixed(4);
      var resultado12 = ((0.2*0.01**0)*(0.1**1)*(0.2**0)*(0.27**0));
   }
   if (elemResult13.textContent === undefined) {
      elemResult13.textContent = "13 =" + Number((resultado10/(resultado10+resultado11+resultado12))).toFixed(4);
   }
   else { // IE
      elemResult13.innerText = "13_1 =" + Number((resultado10/(resultado10+resultado11+resultado12))).toFixed(4);
   }
   if (elemResult14.textContent === undefined) {
      elemResult14.textContent = "14 =" + Number((resultado11/(resultado10+resultado11+resultado12))).toFixed(4);
   }
   else { // IE
      elemResult14.innerText = "14_1 =" + Number((resultado11/(resultado10+resultado11+resultado12))).toFixed(4);
   }
   if (elemResult15.textContent === undefined) {
      elemResult15.textContent = "15 =" + Number((resultado12/(resultado10+resultado11+resultado12))).toFixed(4);
   }
   else { // IE
      elemResult15.innerText = "15_1 =" + Number((resultado12/(resultado10+resultado11+resultado12))).toFixed(4);
   }
   if (elemResult16.textContent === undefined) {
      elemResult16.textContent = "16 =" + Number(((1-1*0.3018)-0.2967)/(((1**2*0.3018**2*0.2**2+(1-1*0.3018)**2*0.2**2+0.2967**2*0.05**2))**(1/2))).toFixed(4);
   }
   else { // IE
      elemResult16.innerText = "16_1 =" + Number(((1-1*0.3018)-0.2967)/(((1**2*0.3018**2*0.2**2+(1-1*0.3018)**2*0.2**2+0.2967**2*0.05**2))**(1/2))).toFixed(4);
   }
   if (elemResult17.textContent === undefined) {
      elemResult17.textContent = "17 =" + Number(((1-2*0.3018)-0.2967)/(((2**2*0.3018**2*0.2**2+(1-2*0.3018)**2*0.2**2+0.2967**2*0.05**2))**(1/2))).toFixed(4);
   }
   else { // IE
      elemResult17.innerText = "17_1=" + Number(((1-2*0.3018)-0.2967)/(((2**2*0.3018**2*0.2**2+(1-2*0.3018)**2*0.2**2+0.2967**2*0.05**2))**(1/2))).toFixed(4);
   }
   if (elemResult18.textContent === undefined) {
      elemResult18.textContent = "18 =" + Number(((1-4*0.3018)-0.2967)/(((4**2*0.3018**2*0.2**2+(1-4*0.3018)**2*0.2**2+0.2967**2*0.05**2))**(1/2))).toFixed(4);
   }
   else { // IE
      elemResult18.innerText = "18_1 =" + Number(((1-4*0.3018)-0.2967)/(((4**2*0.3018**2*0.2**2+(1-4*0.3018)**2*0.2**2+0.2967**2*0.05**2))**(1/2))).toFixed(4);
   }
   if (elemResult19.textContent === undefined) {
      elemResult19.textContent = "19 =" + Number(534.59).toFixed(4) ;
      var resultado19 = + Number(534.59).toFixed(4);
   }
   else { // IE
      elemResult19.innerText = "19_1 =" + Number(534.59).toFixed(4) ;
      var resultado19 = + Number(534.59).toFixed(4);
   }  
   if (num13=="Sim"){
      var fip = 3;
   }
   else {
      var fip = 1;
   }
   if (num14=="Sim"){
      var fdl = 1;
   }
   else {
      var fdl = 3;
   }
   if (num15=="Soldado"){
      var fwd = 1;
   }
   else {
      var fwd = 10;
   }
   if (num16=="Sim"){
      var fam = 1;
   }
   else {
      var fam = 5;
   }
   switch (num17) {
      case "Não aplicável":
         fsm = 1;
         break
      case "Fundação concreto":
         fsm = 1;
         break
      case "Nunca foi feito":
         fsm = 1.5;
         break
      case "Sim, valores conforme API 653":
         fsm = 1;
         break
      case "Sim, valores excedentes API 653":
         fsm = 2;
         break
   }
   if (num18=="Nenhum1"){
      var fom = 1;
   }
   else {
      var fom = 10;
   }
   if (elemResult20.textContent === undefined) {
      elemResult20.textContent = "FIP =" + fip;
   }
   else { // IE
      elemResult20.innerText = "FIP =" + fip;
   }
   if (elemResult21.textContent === undefined) {
      elemResult21.textContent = "FDL =" + fdl;
   }
   else { // IE
      elemResult21.innerText = "FDL =" + fdl;
   }
   if (elemResult22.textContent === undefined) {
      elemResult22.textContent = "FWD =" + fwd;
   }
   else { // IE
      elemResult22.innerText = "FWD =" + fwd;
   }
   if (elemResult23.textContent === undefined) {
      elemResult23.textContent = "FAM =" + fam;
   }
   else { // IE
      elemResult23.innerText = "FAM =" + fam;
   }
   if (elemResult24.textContent === undefined) {
      elemResult24.textContent = "FSM =" + fsm;
   }
   else { // IE
      elemResult24.innerText = "FSM ="+ fsm;
   }
   if (elemResult25.textContent === undefined) {
      elemResult25.textContent = "FOM (Tabela 4.8)= Falta calcular" + 1;
   }
   else { // IE
      elemResult25.innerText = "FOM (Tabela 4.8)= Falta calcular =" + 1;
   }
   if (elemResult26.textContent === undefined) {
      elemResult26.textContent = "DANO = (FIP*FDL*FWD*FAM*FSM*FOM*DTHINfb) = " + resultado19 ;
   }
   else { // IE
      elemResult26.innerText = "DANO = (FIP*FDL*FWD*FAM*FSM*FOM*DTHINfb) =" + resultado19;
   }
   if (elemResult27.textContent === undefined) {
      elemResult27.textContent = "Probabilidade =" + Number(0.0000306*fip*fdl*fwd*fam*fsm*fom*resultado19).toFixed(4);
   }
   else { // IE
      elemResult27.innerText = "Probabilidade =" + Number(0.0000306*fip*fdl*fwd*fam*fsm*fom*resultado19).toFixed(4);

   }
}


