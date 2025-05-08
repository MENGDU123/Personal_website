        async function loadTxtFile() {


            const response = await fetch('example.txt');


            const text = await response.text();


            document.getElementById('content').innerText = text;


        }
//我也许使用了一个很蠢的方式，通过Python读取CPU内存，然后写入txt，再通过js读出来，输出到网页上。
