var convertapi = require('convertapi')('ZBdKtoNyT5GhX2b4');
convertapi.convert('pdf', {
    File: 'Chemistry Project.docx'
}, 'docx').then(function(result) {
    result.saveFiles('c:/Users/Arnav Puri/Desktop/Coding/OSTL Project');
});