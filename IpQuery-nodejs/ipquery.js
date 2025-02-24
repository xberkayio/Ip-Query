const axios = require('axios');
const readline = require('readline');
const fs = require('fs');
const colors = require('colors');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const author = "xberkay-o";

function clearConsole() {
  console.clear();
}

function displayMenu() {
  clearConsole();

  console.log('\x1b[36m********************************************\x1b[0m');
  console.log('\x1b[36m**    IP Information Query and Save       **\x1b[0m');
  console.log('\x1b[36m********************************************\x1b[0m');
  console.log('\x1b[32m1. Query IP and Save\x1b[0m');
  console.log('\x1b[31m2. Exit\x1b[0m');
  console.log('\x1b[36m********************************************\x1b[0m');

  rl.question('\x1b[35mPlease select an option (1/2): \x1b[0m', (choice) => {
    if (choice === '1') {
      rl.question('\x1b[32mPlease enter the IP address or domain: \x1b[0m', (query) => {
        clearConsole();
        queryApi(query);
      });
    } else if (choice === '2') {
      console.log('\x1b[35mExiting...\x1b[0m');
      rl.close();
    } else {
      console.log('\x1b[31mInvalid choice! Please enter 1 or 2.\x1b[0m');
      rl.close();
    }
  });
}

function queryApi(query) {
  const baseUrl = 'http://ip-api.com/json/';
  const fields = [
    'status',
    'continent',
    'continentCode',
    'country',
    'countryCode',
    'region',
    'regionName',
    'city',
    'district',
    'zip',
    'lat',
    'lon',
    'timezone',
    'isp',
    'org',
    'as',
    'asname',
    'reverse',
    'mobile',
    'proxy',
    'hosting',
    'query',
  ];

  const apiUrl = `${baseUrl}${query}?fields=${fields.join(',')}`;

  axios
    .get(apiUrl)
    .then((response) => {
      const data = response.data;

      const formattedData = {
        author: author,
        ...data,
      };

      const fileName = `${data.query}.json`;
      fs.writeFile(fileName, JSON.stringify(formattedData, null, 2), (err) => {
        if (err) {
          console.error('\x1b[31mError writing to file:\x1b[0m', err);
        } else {
          console.log('\x1b[32mData saved to "\x1b[0m%s\x1b[32m" as a JSON file.\x1b[0m', fileName.rainbow);
        }
        rl.close();
      });
    })
    .catch((error) => {
      console.error('\x1b[31mAPI Query Error:\x1b[0m', error);
      rl.close();
    });
}

displayMenu();
