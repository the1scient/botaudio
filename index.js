var Discord = require('discord.js');
var bot = new Discord.Client();
var isReady = true;

bot.on('message', message => {
  if (isReady && message.content === 'BOT PRONTO')
  {
  var voiceChannel = client.channels.get("737825983692013704");
  if (!channel) return console.error("Canal de voz não existe");
  voiceChannel.join().then(connection =>
  {
     const dispatcher = connection.playFile('rojao.mp3');
     dispatcher.on("end", end => {
       voiceChannel.leave();
       });
   }).catch(err => console.log(err));
   isReady = true;
  }
});


bot.login('NzY1Nzg0NDM4MDEyNjQxMjkw.X4Z2VQ.A-2Wr3VacjcfqCBeAH1dwwyPxiU');