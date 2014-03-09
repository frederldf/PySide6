//
//  DemoViewController.m
//  HelloWorld
//
//  Created by admin on 14/1/12.
//  Copyright (c) 2014年 LDF. All rights reserved.
//

#import "DemoViewController.h"
#import "Circle.h"
@interface DemoViewController ()

@end

@implementation DemoViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    //NSLog(@"Hello!");
    
    //char *str="Hello!";
    //NSString *cocoaString;
    //cocoaString=[NSString alloc];
    //cocoaString=[cocoaString initWithCString:str encoding:NSUTF8StringEncoding];
    //NSLog(@"String is %@",cocoaString);
    
    //int sum = [DemoViewController sumWithA:4 andB:7];
    //NSLog(@"sum is=%d",sum);
    
    //int a=[DemoViewController countBmi:55 :5];
    //int b=[DemoViewController countBmiWithHeight:55 andWeight:5];
    
    Circle *circle=[[Circle alloc] initWithRadiusX:5.5f andRaduusY:16.0f];
    float area=[circle area];
    NSLog(@"area is %f",area);
    count=1;
    
    
}
+(int)countBmi : (int)height : (int)weight{
    return 20;
}
+(int)countBmiWithHeight:(int)height andWeight:(int)weight{
    return 20;
}



+(int) sumWithA:(int)A andB:(int)B
{
    int sum;
    sum=A+B;
    return sum;
    
}


- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)btnPush:(UIButton *)sender {
    NSLog(@"button push...");
    count++;
    if(count>3){
        count=1;
    }
    NSString *str=[NSString stringWithFormat:@"a%d.jpg",count];
    self.imgView.image=[UIImage imageNamed:str];
}
@end
