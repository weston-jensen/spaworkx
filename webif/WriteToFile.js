function WriteToFile(passForm)
{
//	set fso=Server.CreateObject("Scripting.FileSystemObject");
	set fso = new ActiveXObject("Scripting.FileSystemObject");
	set s=fso.CreateTextFile("~\Desktop\spaworx\webif\config.txt"), true);

	var regNumber = document.getElementById("regNumber");
	var startTime = document.getElementById("startTime");

	s.WriteLine("Registration Number: " + regNumber);
	s.WriteLine("Start Time: " + startTime);

	s.Close();
}
