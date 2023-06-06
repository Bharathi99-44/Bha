package com.jsp.SundayProject;

import java.util.Scanner;

public class CricketBall {

	public static void main(String[] args) 
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Over");
		int Over=sc.nextInt();
	
		for(int i=1;i<=Over;i++) 
		{
			for(int j=1;j<=6;j++) 
			{
				System.out.println("Over : " +i+" Balls : "+j);
			}
			System.out.println("************");
		}
	}

}
