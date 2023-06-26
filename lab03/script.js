function Evaluate(val) {
    var v = document.getElementById('res');
    var currentValue = v.value;

    if (val === 'power') {
        v.value += '**';
    } else {
        var preview = currentValue + val;
        v.value = preview;
    }
}

 function Output() {
	var num1 = document.getElementById('res').value;
	var num2 = eval(num1);
	document.getElementById('res').value = num2;
 }
 function Clear() {
	var inp = document.getElementById('res');
	inp.value = '';
 }
 function Back() {
	var ev = document.getElementById('res');
	ev.value = ev.value.slice(0,-1);
 }

 function SquareRoot() {
	var num = document.getElementById('res').value;
	var preview = "√(" + num + ")";
	var result = Math.sqrt(parseFloat(num));
	
	if (!isNaN(result)) {
	  document.getElementById('res').value = preview + " = " + result;
	} else {
	  document.getElementById('res').value = 'Invalid';
	}
  }
    
  function Sine() {

	var num = document.getElementById('res').value;
	var preview = "sin(" + num + ")";
	var radians = (parseFloat(num) * Math.PI) / 180; 
	var result = Math.sin(radians).toFixed(4);

	if (!isNaN(result)) {
		document.getElementById('res').value = preview + " = " + result;
	  } else {
		document.getElementById('res').value = 'Invalid';
	  }
  }
  
  function Cosine() {

	var num = document.getElementById('res').value;
	var preview = "cos(" + num + ")";
	var radians = (parseFloat(num) * Math.PI) / 180; 
	var result = Math.cos(radians).toFixed(4);
	
	if (!isNaN(result)) {
		document.getElementById('res').value = preview + " = " + result;
	  } else {
		document.getElementById('res').value = 'Invalid';
	  }
}

function Tangent() {
	var num = document.getElementById('res').value;
	var radians = (parseFloat(num) * Math.PI) / 180;
	var preview = "tan(" + num + ")";
	
	if (Math.abs(Math.cos(radians)) < Number.EPSILON) {
	  document.getElementById('res').value = preview + " = " + "Undefined";
	} else {
	  var result = Math.tan(radians).toFixed(4);
	  document.getElementById('res').value = preview + " = " + result;
	}
  }
  
	