

wolf = importfile(".\wolf.xlsx", "Sheet1", [2, 2001]);
wolf_dl2_dh5 = importfile(".\wolf_dl2_dh5.xlsx", "Sheet1", [2, 2001]);
wolf_dl1_dh4 = importfile(".\wolf_dl1_dh4.xlsx", "Sheet1", [2, 2001]);
local = importfile(".\local.xlsx", "Sheet1", [2, 2001]);
mec = importfile(".\mec.xlsx", "Sheet1", [2, 2001]);


%%

Step = [1:1:2000];
%%plot(Step,wolf,'r')
%%hold on
%%plot(Step,wolf_dl2_dh5,'y')
%%hold on
%%plot(Step,wolf_dl1_dh4,'b')
%hold on
%plot(Step,local,'m')
%hold on
%plot(Step,mec,'g')
%hold 

windowSize = 10;
yy=filter(ones(1,windowSize)/windowSize,1,wolf);
plot(Step,yy,'r')
hold on
yy=filter(ones(1,windowSize)/windowSize,1,mec);
plot(Step,yy,'b')
hold on
yy=filter(ones(1,windowSize)/windowSize,1,wolf_dl2_dh5);
plot(Step,yy,'g')
hold on
yy=filter(ones(1,windowSize)/windowSize,1,wolf_dl1_dh4);
plot(Step,yy,'m')
hold on
axis( [0 2000 -180 120] )

xlabel('Episode')
ylabel('Reward')
%legend('local only','wolf phc ','mec only','wolf-phc-dl2-dh5','wolf-phc-dl1-dh4')
legend('wolf phc ','offloading only','wolf-phc-dl2-dh5','wolf-phc-dl1-dh4')
%figure
