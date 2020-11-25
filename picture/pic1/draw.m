

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

plotyy(Step,wolf,Step,local)
hold on
plot(Step,mec,'g')
hold on
plot(Step,wolf_dl2_dh5,'y')
hold on
plot(Step,wolf_dl1_dh4,'b')
hold on




%axis( [0 2000 -400 200] )

xlabel('Episode')
ylabel('Reward')
legend('wolf-phc','wolf-phc-dl2-dh5','wolf-phc-dl1-dh4','local only','mec only')
%figure
