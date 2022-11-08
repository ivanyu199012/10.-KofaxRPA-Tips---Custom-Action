const { isFileExists, getMsgWithCurrentDateTime } = require("sampleHandler/sampleHandler");
console.log( `isFileExists( "C:/Temp/test.txt" ) = ${ isFileExists( "C:/Temp/test.txt" ) }` );
console.log( `isFileExists( "C:/Temp/test_not_exists.txt" ) = ${ isFileExists( "C:/Temp/test_not_exists.txt" ) }` );
console.log( `getMsgWithCurrentDateTime( "Hello Guys ?" ) = ${ getMsgWithCurrentDateTime( "Hello Guys ?" ) }` );