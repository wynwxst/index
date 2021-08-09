const {app, BrowserWindow} = require('electron')
let {PythonShell} = require('python-shell')

function createWindow () {
    window = new BrowserWindow({width: 1200,height: 700/*,frame:false*/,icon:"../upm.ico",autoHideMenuBar: true})
    window.loadFile('index.html')


    	/*var python = require('child_process').spawn('python', ['./hello.py']);
	python.stdout.on('data',function(data){
    		console.log("data: ",data.toString('utf8'));
	});*/



PythonShell.run('resources/app/gui.py',[],  function  (err, results)  {
 if  (err)  console.log(err);
});

}



app.on('ready', createWindow)

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
      app.quit()
    }
})
