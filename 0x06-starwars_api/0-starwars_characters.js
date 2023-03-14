#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

// Promisify the request module so that
// async await is possible
function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request.get(url, { json: true }, (err, res, body) => {
      if (err) {
        return reject(err);
      }
      resolve(body);
    });
  });
}

async function main () {
  const filmNumber = argv.slice(2)[0];
  const url = `https://swapi-api.alx-tools.com/api/films/${filmNumber}/`;
  const result = await requestPromise(url);
  for (let person of result.characters) {
    person = await requestPromise(person);
    console.log(person.name);
  }
}

// Run main function
main();
