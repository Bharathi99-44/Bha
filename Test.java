package com.jsp.student;

import java.util.Scanner;

public class Test {

	public static void main(String[] args) 
	{
		Scanner sc= new Scanner(System.in);
		System.out.println("Enter the num");
		int num=sc.nextInt();
		
		int sum=0;
		for(;num>0;) 
		{
			int res=num%10;
			sum+=res;
			num/=10;
		}
		System.out.println(sum);
	}

}
