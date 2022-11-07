const { isFileExists, getMsgWithCurrentDateTime } = require("sampleHandler/sampleHandler.js");
console.log( isFileExists( "C:\\MyFiles\\DocTemp\\LF Logistic\\PC1_Login.jpg" ) );
console.log( isFileExists( "C:\\MyFiles\\DocTemp\\LF Logistic\\PC1_FALSE_Login.jpg" ) );
console.log( getMsgWithCurrentDateTime( "Hello Guys ?" ) );