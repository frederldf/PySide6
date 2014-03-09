//
//  DemoViewController.h
//  HelloWorld
//
//  Created by admin on 14/1/12.
//  Copyright (c) 2014年 LDF. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface DemoViewController : UIViewController
{
    int count;
}

@property (weak, nonatomic) IBOutlet UILabel *lblTitle;

- (IBAction)btnPush:(UIButton *)sender;

@property (strong, nonatomic) IBOutlet UIImageView *imgView;
@end
