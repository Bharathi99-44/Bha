package com.jsp.student;

class C
{
	public static void m1() 
	{
		System.out.println("A");
	}
}
class D extends C
{
	
	public static void m1() 
	{
		System.out.println("B");
	}
}
public class Test1 {

	public static void main(String[] args) 
	{
		D.m1();
		C.m1();
	}

}
