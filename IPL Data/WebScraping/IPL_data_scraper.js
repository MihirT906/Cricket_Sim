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
  const {homeTeams, homeScores, homeOvers, awayTeams, awayScores, awayOvers, dates, stadiums, winners} = await page.evaluate(() => {
    const teams = Array.from(document.querySelectorAll(".vn-teamTitle h3")).map(
      (x) => x.textContent
    );
    
    const scores = Array.from(document.querySelectorAll(".vn-teamTitle p")).map(
      (x) => x.textContent
    );
    const overs = Array.from(document.querySelectorAll(".vn-teamTitle span")).map(
      (x) => x.textContent
    );
    const dates = Array.from(document.querySelectorAll(".vn-date.ng-binding.ng-scope")).map(
      (x) => x.textContent
    );
    const stadiums = Array.from(document.querySelectorAll(".vn-matchTime p span")).map(
      (x) => x.textContent
    );
    const winners = Array.from(document.querySelectorAll(".vn-ticket div")).map(
      (x) => x.textContent
    );
    const homeTeams = [];
    const awayTeams = [];
    const homeScores = [];
    const awayScores = [];
    const homeOvers = [];
    const awayOvers = [];
    for (i=2;i<teams.length;i+=4){
        homeTeams.push(teams[i].slice(0,-2));
        awayTeams.push(teams[i+1]);
        homeScores.push(scores[i] ? scores[i].slice(0,-1): 0);
        awayScores.push(scores[i+1] ? scores[i+1]: 0);
        homeOvers.push(overs[i] ? overs[i].slice(1,-5): 0);
        awayOvers.push(scores[i+1] ? overs[i+1].slice(1,-5): 0);
    }

    return {homeTeams, homeScores, homeOvers, awayTeams, awayScores, awayOvers, dates, stadiums, winners};
  });
  console.log(homeOvers.length);
  console.log(awayOvers.length);
  //console.log(winners)
  //FOrmatting into CSV
  const csv_string = [];
  csv_string.push("date,year,HomeTeam,HomeScore,HomeOvers,AwayTeam,AwayScore,AwayOvers,winner,venue\r\n");
  for(i=0;i<homeTeams.length;i++){
    let data = dates[2*i] + "," + homeTeams[i] + "," + homeScores[i] + "," + homeOvers[i] + "," +  awayTeams[i] + "," + awayScores[i] + "," + awayOvers[i] + "," + winners[2*i] + "," + stadiums[2*i] + "\r\n"
    csv_string.push(data);
    
  }
  
  fs.writeFile('IPL_data_scraped2022.csv', csv_string, (err) => {
      
    // In case of a error throw err.
    if (err) throw err;
})
  //console.log(matchStats);
  //console.log(awayTeams);
  

  await browser.close();
})();
