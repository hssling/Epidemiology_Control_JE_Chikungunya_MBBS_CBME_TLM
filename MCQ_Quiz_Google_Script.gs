/**
 * Google Apps Script for MCQ Quiz on JE and Chikungunya
 * This script creates a quiz in Google Sheets with questions, options, and scoring.
 */

function createQuiz() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  if (!spreadsheet) {
    spreadsheet = SpreadsheetApp.create('JE and Chikungunya Quiz');
  }
  var sheet = spreadsheet.getActiveSheet();
  sheet.clear();

  // Set headers
  sheet.getRange('A1').setValue('Question');
  sheet.getRange('B1').setValue('Option A');
  sheet.getRange('C1').setValue('Option B');
  sheet.getRange('D1').setValue('Option C');
  sheet.getRange('E1').setValue('Option D');
  sheet.getRange('F1').setValue('Correct Answer');
  sheet.getRange('G1').setValue('User Answer');
  sheet.getRange('H1').setValue('Result');

  // Quiz data
  var quizData = [
    ['What is the primary vector for Japanese Encephalitis?', 'Aedes aegypti', 'Culex tritaeniorhynchus', 'Anopheles gambiae', 'Mansonia', 'B', '', ''],
    ['Which disease is characterized by chronic joint pain?', 'Japanese Encephalitis', 'Chikungunya', 'Dengue', 'Zika', 'B', '', ''],
    ['What is the case-fatality rate for JE?', '10%', '30%', '50%', '70%', 'B', '', ''],
    ['For Chikungunya, diagnosis in the first week uses:', 'RT-PCR', 'IgM ELISA', 'CSF Analysis', 'Blood smear', 'A', '', ''],
    ['Common prevention measure for both diseases:', 'Vaccination only', 'Vector control', 'Antivirals', 'Isolation', 'B', '', ''],
    ['JE is endemic in how many countries?', '10', '24', '50', '100', 'B', '', ''],
    ['Annual JE cases globally are approximately:', '10,000', '100,000', '1,000,000', '10,000,000', 'B', '', ''],
    ['JE transmission cycle involves:', 'Mosquito-Human', 'Mosquito-Pig/Bird', 'Human-Human', 'Bird-Human', 'B', '', ''],
    ['Incubation period for JE is:', '1-3 days', '4-14 days', '15-30 days', '30-60 days', 'B', '', ''],
    ['Severe JE symptoms include:', 'Joint pain', 'Encephalitis', 'Rash', 'Fever', 'B', '', ''],
    ['Diagnosis for JE uses:', 'RT-PCR', 'IgM ELISA', 'Blood culture', 'X-ray', 'B', '', ''],
    ['Treatment for JE is:', 'Antiviral', 'Supportive', 'Antibiotics', 'Surgery', 'B', '', ''],
    ['JE vaccines are:', 'Inactivated', 'Live attenuated', 'Both', 'None', 'C', '', ''],
    ['Vector for Chikungunya is:', 'Culex', 'Aedes', 'Anopheles', 'Mansonia', 'B', '', ''],
    ['Chikungunya outbreaks are common in:', 'Winter', 'Rainy season', 'Dry season', 'Summer', 'B', '', ''],
    ['Chikungunya pain lasts:', 'Days', 'Weeks to years', 'Hours', 'Minutes', 'B', '', ''],
    ['Chikungunya diagnosis after first week:', 'RT-PCR', 'Serology', 'CSF', 'Urine test', 'B', '', ''],
    ['Treatment for Chikungunya avoids:', 'Paracetamol', 'NSAIDs', 'Fluids', 'Antibiotics', 'B', '', ''],
    ['Prevention for Chikungunya includes:', 'Vaccination', 'Eliminate breeding sites', 'Antivirals', 'Masks', 'B', '', ''],
    ['Both diseases are preventable by:', 'Vector control', 'Vaccination only', 'Antibiotics', 'Quarantine', 'A', '', '']
  ];

  // Populate sheet
  sheet.getRange(2, 1, quizData.length, 8).setValues(quizData);

  // Format
  sheet.getRange('A1:H1').setFontWeight('bold');
  sheet.autoResizeColumns(1, 8);
}

function scoreQuiz() {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  if (!spreadsheet) {
    throw new Error('No active spreadsheet. Please open a Google Sheet and run the script.');
  }
  var sheet = spreadsheet.getActiveSheet();
  var data = sheet.getDataRange().getValues();
  var score = 0;

  for (var i = 1; i < data.length; i++) {
    var correct = data[i][5]; // Correct answer is now in column F (index 5)
    var user = data[i][6];    // User answer is now in column G (index 6)
    var result = (user === correct) ? 'Correct' : 'Incorrect';
    sheet.getRange(i+1, 8).setValue(result); // Result in column H (index 7)
    if (user === correct) score++;
  }

  sheet.getRange(data.length + 1, 1).setValue('Total Score: ' + score + '/' + (data.length - 1));
}

function createGoogleForm() {
  var form = FormApp.create('MCQ Quiz: JE and Chikungunya');
  form.setDescription('Test your knowledge on Japanese Encephalitis and Chikungunya.');
  form.setIsQuiz(true); // Enable quiz mode for automatic scoring

  var questions = [
    {q: 'What is the primary vector for Japanese Encephalitis?', a: ['Aedes aegypti', 'Culex tritaeniorhynchus', 'Anopheles gambiae', 'Mansonia'], correct: 1},
    {q: 'Which disease is characterized by chronic joint pain?', a: ['Japanese Encephalitis', 'Chikungunya', 'Dengue', 'Zika'], correct: 1},
    {q: 'What is the case-fatality rate for JE?', a: ['10%', '30%', '50%', '70%'], correct: 1},
    {q: 'For Chikungunya, diagnosis in the first week uses:', a: ['RT-PCR', 'IgM ELISA', 'CSF Analysis', 'Blood smear'], correct: 0},
    {q: 'Common prevention measure for both diseases:', a: ['Vaccination only', 'Vector control', 'Antivirals', 'Isolation'], correct: 1},
    {q: 'JE is endemic in how many countries?', a: ['10', '24', '50', '100'], correct: 1},
    {q: 'Annual JE cases globally are approximately:', a: ['10,000', '100,000', '1,000,000', '10,000,000'], correct: 1},
    {q: 'JE transmission cycle involves:', a: ['Mosquito-Human', 'Mosquito-Pig/Bird', 'Human-Human', 'Bird-Human'], correct: 1},
    {q: 'Incubation period for JE is:', a: ['1-3 days', '4-14 days', '15-30 days', '30-60 days'], correct: 1},
    {q: 'Severe JE symptoms include:', a: ['Joint pain', 'Encephalitis', 'Rash', 'Fever'], correct: 1},
    {q: 'Diagnosis for JE uses:', a: ['RT-PCR', 'IgM ELISA', 'Blood culture', 'X-ray'], correct: 1},
    {q: 'Treatment for JE is:', a: ['Antiviral', 'Supportive', 'Antibiotics', 'Surgery'], correct: 1},
    {q: 'JE vaccines are:', a: ['Inactivated', 'Live attenuated', 'Both', 'None'], correct: 2},
    {q: 'Vector for Chikungunya is:', a: ['Culex', 'Aedes', 'Anopheles', 'Mansonia'], correct: 1},
    {q: 'Chikungunya outbreaks are common in:', a: ['Winter', 'Rainy season', 'Dry season', 'Summer'], correct: 1},
    {q: 'Chikungunya pain lasts:', a: ['Days', 'Weeks to years', 'Hours', 'Minutes'], correct: 1},
    {q: 'Chikungunya diagnosis after first week:', a: ['RT-PCR', 'Serology', 'CSF', 'Urine test'], correct: 1},
    {q: 'Treatment for Chikungunya avoids:', a: ['Paracetamol', 'NSAIDs', 'Fluids', 'Antibiotics'], correct: 1},
    {q: 'Prevention for Chikungunya includes:', a: ['Vaccination', 'Eliminate breeding sites', 'Antivirals', 'Masks'], correct: 1},
    {q: 'Both diseases are preventable by:', a: ['Vector control', 'Vaccination only', 'Antibiotics', 'Quarantine'], correct: 0}
  ];

  questions.forEach(function(item) {
    var question = form.addMultipleChoiceItem();
    question.setTitle(item.q)
            .setChoices(item.a.map(function(choice, index) {
              return question.createChoice(choice, index === item.correct);
            }))
            .setPoints(1); // Assign points for correct answers
  });

  // Publish the form and get URLs
  form.setPublishingSummary(true);
  var publishedUrl = form.getPublishedUrl();
  var editUrl = form.getEditUrl();

  Logger.log('Published Form URL (shareable): ' + publishedUrl);
  Logger.log('Edit URL: ' + editUrl);

  // Also log to console for easy copying
  console.log('Published Form URL: ' + publishedUrl);
  console.log('Edit URL: ' + editUrl);
}

// To use: Run createGoogleForm() to generate a Google Form with the quiz. The form URL will be logged in the console.
