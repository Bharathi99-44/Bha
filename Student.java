package com.jsp.student;

class A 
{
	int id;
	String name;
	int age;
	String gender;
	String phno;
	static String StudentCollegeName;
	static String StudentCollegeAddress;
	
	public void addStudents(int id,String name,int age,String gender,String phno) 
	{
		this.id= id;
		this.name=name;
		this.age=age;
		this.gender=gender;
		this.phno=phno;
	}
	public void displayStudents() 
	{
		System.out.println("Student ID : "+this.id);
		System.out.println("Student Name : "+this.name);
		System.out.println("Student Age : "+this.age);
		System.out.println("Student Gender : "+this.gender);
		System.out.println("Student phno : "+this.phno);
		System.out.println("Student  StudentCollegeName: "+this.StudentCollegeName);
		System.out.println("Student StudentCollegeAddress : "+this.StudentCollegeAddress);
		System.out.println("****************************************************");
	}
	
	public  static void changeCollegeName(String StudentCollegeName)
	{
		A.StudentCollegeName=StudentCollegeName;
	}
	public static void changeCollegeAddress(String StudentCollegeAddress)
	{
		A.StudentCollegeAddress=StudentCollegeAddress;
	}
	
}
public class Student 
{

	public static void main(String[] args) 
	{
		A.StudentCollegeName = "JSP";
		A. StudentCollegeAddress = "OAR";
		
		A s1 = new A();
		s1.addStudents(1,"Bharathi",23,"Female","9999999999");
		s1.displayStudents();
		
		A s2 = new A();
		s2.addStudents(2,"Jyoshna",20,"Female","9999999999");
		s2.displayStudents();
	}

}
