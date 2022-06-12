const puppeteer = require("puppeteer");
const fs = require("fs/promises");

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: false,
  });
  const page = await browser.newPage();
  await page.goto("https://www.iplt20.com/matches/results/men/2022");

  await page.waitForSelector(".live-score");
  const {homeTeams, homeScores, homeOvers, awayTeams, awayScores, awayOvers} = await page.evaluate(() => {
    const teams = Array.from(document.querySelectorAll(".vn-teamTitle h3")).map(
      (x) => x.textContent
    );
    
    const scores = Array.from(document.querySelectorAll(".vn-teamTitle p")).map(
      (x) => x.textContent
    );
    const overs = Array.from(document.querySelectorAll(".vn-teamTitle span")).map(
      (x) => x.textContent
    );
    const homeTeams = [];
    const awayTeams = [];
    const homeScores = [];
    const awayScores = [];
    const homeOvers = [];
    const awayOvers = [];
    for (i=2;i<teams.length;i+=4 ){
        homeTeams.push(teams[i].slice(0,-2));
        awayTeams.push(teams[i+1]);
        homeScores.push(scores[i].slice(0,-1));
        awayScores.push(scores[i+1]);
        homeOvers.push(overs[i].slice(1,-5));
        awayOvers.push(overs[i+1].slice(1,-5));
    }
    return {homeTeams, homeScores, homeOvers, awayTeams, awayScores, awayOvers};
  });
  console.log(homeOvers.length);
  console.log(awayOvers.length);
  //FOrmatting into CSV
  const csv_string = [];
  for(i=0;i<homeTeams.length;i++){
    let data = homeTeams[i] + "," + homeScores[i] + "," + homeOvers[i] + "," +  awayTeams[i] + "," + awayScores[i] + "," + awayOvers[i] + "\r\n"
    csv_string.push(data);
    
  }
  
  fs.writeFile('IPL_data.csv', csv_string, (err) => {
      
    // In case of a error throw err.
    if (err) throw err;
})
  //console.log(matchStats);
  //console.log(awayTeams);
  

  await browser.close();
})();
