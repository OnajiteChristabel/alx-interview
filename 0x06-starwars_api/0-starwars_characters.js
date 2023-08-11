#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;
let characterUrls = [];
const characterNames = [];

const fetchCharacterUrls = () => {
  return new Promise((resolve, reject) => {
    request(filmEndPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject(err || `Status Code - ${res.statusCode}`);
      } else {
        const jsonBody = JSON.parse(body);
        characterUrls = jsonBody.characters;
        resolve();
      }
    });
  });
};

const fetchCharacterNames = () => {
  if (characterUrls.length > 0) {
    const fetchPromises = characterUrls.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (err, res, body) => {
          if (err || res.statusCode !== 200) {
            reject(err || `Status Code - ${res.statusCode}`);
          } else {
            const jsonBody = JSON.parse(body);
            characterNames.push(jsonBody.name);
            resolve();
          }
        });
      });
    });
    return Promise.all(fetchPromises);
  } else {
    console.error('Error: No character URLs found.');
  }
};

const printCharacterNames = () => {
  characterNames.forEach((name, index) => {
    process.stdout.write(name);
    if (index < characterNames.length - 1) {
      process.stdout.write('\n');
    }
  });
};

const fetchAndPrintCharacterNames = async () => {
  try {
    await fetchCharacterUrls();
    await fetchCharacterNames();
    printCharacterNames();
  } catch (error) {
    console.error('Error:', error);
  }
};

fetchAndPrintCharacterNames();
